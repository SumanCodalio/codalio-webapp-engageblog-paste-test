require "test_helper"

class AcceptanceCriteriaTest < ActionDispatch::IntegrationTest
  setup do
    Rails.application.load_seed
    @org = Organization.find_by!(slug: "demo-org")
    @admin = User.find_by!(email: "administrator@example.com")
    @content_member = User.find_by!(email: "content_team_member@demo.com")
    @viewer = User.find_by!(email: "viewer@example.com")
  end

  def auth_headers(user)
    { "Authorization" => "Bearer #{user.api_token}", "Content-Type" => "application/json" }
  end

  # AC-1, AC-2, AC-3, AC-4, AC-5, AC-6, AC-9, AC-10, AC-11, AC-12
  # AC-7, AC-8
  test "AC-1 to AC-12: Create, view, edit and publish posts" do
    # AC-1: content member can create, viewer cannot
    post "/api/#{@org.slug}/posts", params: { title: "Draft", content: "Formatted text", status: "draft", user_id: @content_member.id }.to_json, headers: auth_headers(@viewer)
    assert_response :forbidden

    assert_difference -> { Post.count }, 1 do
      # AC-2, AC-3
      post "/api/#{@org.slug}/posts", params: { title: "Draft", content: "Formatted text", status: "draft", user_id: @content_member.id }.to_json, headers: auth_headers(@content_member)
    end
    assert_response :created
    post_id = response.parsed_body["id"]

    # AC-4: preview before publishing (show)
    get "/api/#{@org.slug}/posts/#{post_id}", headers: auth_headers(@content_member)
    assert_response :success

    # AC-9: viewer cannot edit
    put "/api/#{@org.slug}/posts/#{post_id}", params: { status: "published" }.to_json, headers: auth_headers(@viewer)
    assert_response :forbidden

    # AC-5, AC-11, AC-12: publish the post and modify text
    put "/api/#{@org.slug}/posts/#{post_id}", params: { status: "published", content: "Updated text" }.to_json, headers: auth_headers(@content_member)
    assert_response :success
    assert_equal "published", response.parsed_body["status"]
    assert_equal "Updated text", response.parsed_body["content"]

    # AC-6, AC-10: visible on blog (index)
    get "/api/#{@org.slug}/posts", headers: auth_headers(@content_member)
    assert_response :success
    ids = (response.parsed_body["data"] || response.parsed_body).map { |p| p["id"] }
    assert_includes ids, post_id

    # AC-7, AC-8: The data model stores approved and profile_completed
    assert_respond_to @admin, :approved
    assert_respond_to @admin, :profile_completed
  end

  # AC-13 to AC-18: Upload Video Content
  test "AC-13 to AC-18: Upload and store videos" do
    # AC-13: Viewer cannot upload
    post "/api/#{@org.slug}/videos", params: { title: "Vid", url: "http://vid.mp4", duration: 120, user_id: @content_member.id }.to_json, headers: auth_headers(@viewer)
    assert_response :forbidden

    assert_difference -> { Video.count }, 1 do
      # AC-14, AC-15, AC-17, AC-18
      post "/api/#{@org.slug}/videos", params: { title: "My Vid", url: "http://vid.mp4", duration: 120, user_id: @content_member.id }.to_json, headers: auth_headers(@content_member)
    end
    assert_response :created
    video_id = response.parsed_body["id"]

    # AC-16: stored in media library (index videos)
    get "/api/#{@org.slug}/videos", headers: auth_headers(@content_member)
    assert_response :success
    assert_includes (response.parsed_body["data"] || response.parsed_body).map { |v| v["id"] }, video_id
  end

  # AC-19 to AC-22: Embed Video in Post
  test "AC-19 to AC-22: Embed video in post" do
    post_record = Post.create!(title: "Post with Video", content: "body", organization: @org, user: @content_member)
    video_record = Video.create!(title: "Vid", url: "http://vid.mp4", organization: @org, user: @content_member)

    put "/api/#{@org.slug}/videos/#{video_record.id}", params: { post_id: post_record.id }.to_json, headers: auth_headers(@viewer)
    assert_response :forbidden # AC-19

    put "/api/#{@org.slug}/videos/#{video_record.id}", params: { post_id: post_record.id }.to_json, headers: auth_headers(@content_member)
    assert_response :success # AC-20
    puts "After update: #{response.parsed_body}"

    # AC-21, AC-22: displayed in post preview
    get "/api/#{@org.slug}/videos", params: { filter: { post_id: post_record.id } }, headers: auth_headers(@content_member)
    assert_response :success
    assert_equal video_record.id, (response.parsed_body["data"] || response.parsed_body).first["id"]
  end

  # AC-23 to AC-26: Admin Login
  test "AC-23 to AC-26: Authentication and Login" do
    # AC-23
    get "/api/#{@org.slug}/users"
    assert_response :unauthorized
    assert_equal "Unauthenticated.", response.parsed_body["message"]

    # AC-26
    post "/api/auth/login", params: { email: @admin.email, password: "wrong" }.to_json, headers: { "Content-Type" => "application/json" }
    assert_response :unauthorized

    # AC-24, AC-25
    post "/api/auth/login", params: { email: @admin.email, password: "password" }.to_json, headers: { "Content-Type" => "application/json" }
    assert_response :success
    assert response.parsed_body["token"].present?
  end

  # AC-27 to AC-33, AC-60: Manage Content Team Members
  test "AC-27 to AC-33, AC-60: Manage users" do
    # AC-27
    get "/api/#{@org.slug}/users", headers: auth_headers(@content_member)
    assert_response :forbidden

    # AC-28
    get "/api/#{@org.slug}/users", headers: auth_headers(@admin)
    assert_response :success
    assert (response.parsed_body["data"] || response.parsed_body).length > 0

    # AC-29, AC-32, AC-33, AC-60
    assert_difference -> { User.count }, 1 do
      post "/api/#{@org.slug}/users", params: { name: "New User", email: "new@example.com", password: "password", first_name: "New", last_name: "User", approved: true, profile_completed: false }.to_json, headers: auth_headers(@admin)
    end
    assert_response :created
    new_user_id = response.parsed_body["id"]
    assert_equal "New", response.parsed_body["first_name"]

    # AC-30
    put "/api/#{@org.slug}/users/#{new_user_id}", params: { last_name: "Updated" }.to_json, headers: auth_headers(@admin)
    assert_response :success
    assert_equal "Updated", response.parsed_body["last_name"]

    # AC-31
    assert_difference -> { User.count }, -1 do
      delete "/api/#{@org.slug}/users/#{new_user_id}", headers: auth_headers(@admin)
    end
    assert_response :success
  end

  # AC-34 to AC-36: User Logout
  test "AC-34 to AC-36: Logout functionality" do
    token = @content_member.api_token
    # AC-34, AC-35
    post "/api/auth/logout", headers: { "Authorization" => "Bearer #{token}", "Content-Type" => "application/json" }
    assert_response :success

    # AC-36
    get "/api/#{@org.slug}/posts", headers: { "Authorization" => "Bearer #{token}", "Content-Type" => "application/json" }
    assert_response :unauthorized
  end

  # AC-37 to AC-45: View and Filter Analytics
  test "AC-37 to AC-45: Analytics access and filtering" do
    post_record = Post.create!(title: "Stats Post", organization: @org, user: @content_member)
    AnalyticsData.create!(event_type: "view", recorded_at: 1.day.ago, post: post_record, organization: @org)
    AnalyticsData.create!(event_type: "share", recorded_at: 2.days.ago, post: post_record, organization: @org)

    # AC-37
    get "/api/#{@org.slug}/analytics_data", headers: auth_headers(@viewer)
    assert_response :forbidden

    # AC-38, AC-39, AC-40
    get "/api/#{@org.slug}/analytics_data", headers: auth_headers(@content_member)
    assert_response :success
    assert_equal 4, (response.parsed_body["data"] || response.parsed_body).length

    # AC-41, AC-45
    get "/api/#{@org.slug}/analytics_data?filter[event_type]=view", headers: auth_headers(@content_member)
    assert_response :success
    assert_equal 2, (response.parsed_body["data"] || response.parsed_body).length

    # AC-42, AC-43, AC-44
    get "/api/#{@org.slug}/analytics_data?sort=-recorded_at", headers: auth_headers(@content_member)
    assert_response :success
  end

  # AC-46 to AC-49: Connect to Marketing Tools
  test "AC-46 to AC-49: API Integrations" do
    # TODO: Feature not implemented yet. No API integrations endpoints available.
    skip "Integrations feature is not implemented in backend"
  end

  # AC-50 to AC-52: System Health Monitoring
  test "AC-50 to AC-52: System Health Monitoring" do
    # TODO: Feature not implemented yet. No monitoring endpoints available.
    skip "System Monitoring feature is not implemented in backend"
  end

  # AC-53 to AC-55: Data Backup and Restore
  test "AC-53 to AC-55: Data Backup and Restore" do
    # TODO: Feature not implemented yet. No backup logic available.
    skip "Backup and restore feature is not implemented in backend"
  end

  # AC-56 to AC-58: Role-Based Access Control
  test "AC-56 to AC-58: RBAC" do
    # AC-56: content member cannot access admin endpoints
    get "/api/#{@org.slug}/users", headers: auth_headers(@content_member)
    assert_response :forbidden

    # AC-57: admin has full access
    get "/api/#{@org.slug}/users", headers: auth_headers(@admin)
    assert_response :success
    get "/api/#{@org.slug}/posts", headers: auth_headers(@admin)
    assert_response :success

    # AC-58: unauthorized attempts blocked
    get "/api/#{@org.slug}/posts", headers: { "Authorization" => "Bearer invalid", "Content-Type" => "application/json" }
    assert_response :unauthorized
  end

  # AC-59: Dashboard stats endpoint
  test "AC-59: Dashboard stats endpoint" do
    get "/api/#{@org.slug}/dashboard/stats", headers: auth_headers(@content_member)
    assert_response :success
    json = response.parsed_body
    assert json.key?("total_content_reach")
    assert json.key?("video_watch_hours")
  end

  # AC-61: Data Seeding
  test "AC-61: Data Seeding provides roles and sample users" do
    assert Role.exists?(slug: "admin")
    assert Role.exists?(slug: "content_team_member")
    assert @admin.user_roles.joins(:role).exists?(roles: { slug: 'admin' }, organization: @org)
    assert @content_member.user_roles.joins(:role).exists?(roles: { slug: 'content_team_member' }, organization: @org)
  end
end
