# frozen_string_literal: true

# Create organizations
demo_org = Organization.find_or_create_by!(slug: 'demo-org') do |o|
  o.name = 'Demo Organization'
end

other_org = Organization.find_or_create_by!(slug: 'runtime-other-org') do |o|
  o.name = 'Other Organization'
end

# Create roles
admin_role = Role.find_or_create_by!(slug: 'admin') do |r|
  r.name = 'Admin'
end

content_member_role = Role.find_or_create_by!(slug: 'content_team_member') do |r|
  r.name = 'Content Team Member'
end

viewer_role = Role.find_or_create_by!(slug: 'viewer') do |r|
  r.name = 'Viewer'
end

# Assign permissions to roles via OrgRolePermission for demo_org
OrgRolePermission.find_or_create_by!(organization: demo_org, role: admin_role) do |p|
  p.permissions = ['*']
end

OrgRolePermission.find_or_create_by!(organization: demo_org, role: content_member_role) do |p|
  p.permissions = [
    'posts.index', 'posts.show', 'posts.store', 'posts.update', 'posts.destroy', 'posts.trashed', 'posts.restore',
    'videos.index', 'videos.show', 'videos.store', 'videos.update', 'videos.destroy', 'videos.trashed', 'videos.restore',
    'analytics_data.index', 'analytics_data.show'
  ]
end

OrgRolePermission.find_or_create_by!(organization: demo_org, role: viewer_role) do |p|
  p.permissions = ['posts.index', 'posts.show', 'videos.index', 'videos.show']
end

OrgRolePermission.find_or_create_by!(organization: other_org, role: admin_role) do |p|
  p.permissions = ['*']
end

# Helper to create/update users
def create_user(email, first_name)
  user = User.find_or_initialize_by(email: email)
  user.name = first_name
  user.first_name = first_name
  if user.new_record? || user.password_digest.blank?
    seed_password = ENV["SEED_PASSWORD"] || ("password" unless Rails.env.production?)
    raise "SEED_PASSWORD is required in production" unless seed_password
    user.password = seed_password
  end
  user.save!
  user
end

admin_user = create_user('administrator@example.com', 'Admin')
viewer_user = create_user('viewer@example.com', 'Viewer')
outsider_user = create_user('outsider@example.com', 'Outsider')
content_user = create_user('content_team_member@demo.com', 'Content')

# Memberships
UserRole.find_or_create_by!(user: admin_user, organization: demo_org, role: admin_role)
UserRole.find_or_create_by!(user: viewer_user, organization: demo_org, role: viewer_role)
UserRole.find_or_create_by!(user: content_user, organization: demo_org, role: content_member_role)
UserRole.find_or_create_by!(user: outsider_user, organization: other_org, role: admin_role)

# Seed representative records
# Posts
post1 = Post.find_or_create_by!(organization: demo_org, title: 'Demo Post 1') do |p|
  p.user = admin_user
  p.content = 'Welcome to the demo blog'
  p.status = 'published'
end

post2 = Post.find_or_create_by!(organization: other_org, title: 'Other Post 1') do |p|
  p.user = outsider_user
  p.content = 'Welcome to the other blog'
  p.status = 'draft'
end

# Videos
Video.find_or_create_by!(organization: demo_org, url: 'https://example.com/demo.mp4') do |v|
  v.title = 'Demo Video'
  v.user = admin_user
  v.post = post1
  v.duration = 120
end

Video.find_or_create_by!(organization: other_org, url: 'https://example.com/other.mp4') do |v|
  v.title = 'Other Video'
  v.user = outsider_user
  v.post = post2
  v.duration = 60
end

# AnalyticsData
AnalyticsData.find_or_create_by!(organization: demo_org, event_type: 'view', post: post1) do |a|
  a.recorded_at = Time.current.beginning_of_day
  a.event_data = { user_agent: 'Firefox' }
end

AnalyticsData.find_or_create_by!(organization: demo_org, event_type: 'complete', post: post1) do |a|
  a.recorded_at = Time.current.beginning_of_day
  a.event_data = { user_agent: 'Firefox' }
end

sarah = User.find_or_initialize_by(email: "sarah.chen@contentreach.io")
sarah.name = "Sarah Chen"
sarah.first_name = "Sarah"
sarah.last_name = "Chen"
if sarah.new_record? || sarah.password_digest.blank?
  seed_password = ENV["SEED_PASSWORD"] || ("password" unless Rails.env.production?)
  raise "SEED_PASSWORD is required in production" unless seed_password
  sarah.password = seed_password
end
sarah.save!

alex = User.find_or_initialize_by(email: "alex.thorne@contentreach.io")
alex.name = "Alex Thorne"
alex.first_name = "Alex"
alex.last_name = "Thorne"
if alex.new_record? || alex.password_digest.blank?
  seed_password = ENV["SEED_PASSWORD"] || ("password" unless Rails.env.production?)
  raise "SEED_PASSWORD is required in production" unless seed_password
  alex.password = seed_password
end
alex.save!

demo_org_again = Organization.find_by!(slug: 'demo-org')

UserRole.find_or_create_by!(user: sarah, organization: demo_org_again, role: content_member_role)
UserRole.find_or_create_by!(user: alex, organization: demo_org_again, role: admin_role)
