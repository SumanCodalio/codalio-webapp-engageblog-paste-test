class Api::DashboardController < Rhino::ResourcesController
  skip_before_action :set_model_class, :set_model, :authorize_action, raise: false

  def stats
    user = current_user
    org = Rhino.context.organization

    unless user
      render json: { message: "Unauthenticated." }, status: :unauthorized
      return
    end

    unless org
      render json: { message: "Organization not found" }, status: :not_found
      return
    end

    unless user.has_permission?('analytics_data.index', org)
      render json: { message: "Not found" }, status: :not_found
      return
    end

    Rhino.for_user(user).in_organization(org).run do
      analytics = Rhino.query(AnalyticsData)
      videos = Rhino.query(Video)
      posts = Rhino.query(Post)

      total_reach = analytics.where(event_type: 'view').count
      
      watch_seconds = videos.sum(:duration) || 0
      watch_hours = (watch_seconds / 3600.0).round(1)

      completes = analytics.where(event_type: 'complete').count
      views = total_reach > 0 ? total_reach : 1
      avg_read_completion = ((completes.to_f / views) * 100).round(1)

      render json: {
        total_content_reach: total_reach,
        video_watch_hours: watch_hours,
        avg_read_completion: "#{avg_read_completion}%"
      }
    end
  end
end
