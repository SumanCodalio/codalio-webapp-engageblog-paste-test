# frozen_string_literal: true

class PostPolicy < Rhino::ResourcePolicy
  self.resource_slug = 'posts'

  def permitted_attributes_for_show(user)
    return ['*'] if has_role?(user, 'admin') || has_role?(user, 'content_team_member') || has_role?(user, 'viewer')
    []
  end
  def hidden_attributes_for_show(user)
    []
  end
  def permitted_attributes_for_create(user)
    return ['*'] if has_role?(user, 'admin')
    return ['title', 'content', 'status', 'published_at', 'user_id'] if has_role?(user, 'content_team_member')
    []
  end
  def permitted_attributes_for_update(user)
    return ['*'] if has_role?(user, 'admin')
    return ['title', 'content', 'status', 'published_at', 'user_id'] if has_role?(user, 'content_team_member')
    []
  end
end
