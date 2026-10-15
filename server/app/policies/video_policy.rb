# frozen_string_literal: true

class VideoPolicy < Rhino::ResourcePolicy
  self.resource_slug = 'videos'

  def permitted_attributes_for_show(user)
    return ['*'] if has_role?(user, 'admin') || has_role?(user, 'content_team_member')
    []
  end
def hidden_attributes_for_show(user)
  []
end
  def permitted_attributes_for_create(user)
    return ['*'] if has_role?(user, 'admin')
    return ['title', 'url', 'duration', 'post_id', 'user_id'] if has_role?(user, 'content_team_member')
    []
  end
  def permitted_attributes_for_update(user)
    return ['*'] if has_role?(user, 'admin')
    return ['title', 'url', 'duration', 'post_id', 'user_id'] if has_role?(user, 'content_team_member')
    []
  end
end
