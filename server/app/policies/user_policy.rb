# frozen_string_literal: true

# Policy for the User model.
#
# Required for Rhino's per-include authorization: when a resource exposes a
# User relation (e.g. ?include=assignee on Task, ?include=author on Comment,
# ?include=owner on Project), Pundit looks up UserPolicy. Without this class
# Pundit raises Pundit::NotDefinedError and the include returns 403, even for
# roles that have the `users.index` / `users.show` permission granted.
#
# Customize per-action behavior or attribute permissions as needed; defaults
# inherited from Rhino::ResourcePolicy enforce `users.<action>` permission
# slugs against the user's `user_roles.permissions` array.
class UserPolicy < Rhino::ResourcePolicy
  def permitted_attributes_for_create(user)
    if has_role?(user, 'admin')
      %w[name first_name last_name email password approved profile_completed]
    else
      []
    end
  end

  def permitted_attributes_for_update(user)
    if has_role?(user, 'admin')
      %w[name first_name last_name email password approved profile_completed]
    else
      %w[name first_name last_name email password profile_completed]
    end
  end

  def update?
    super || (user && record.id == user.id) || has_role?(user, 'admin')
  end

  def create?
    super || has_role?(user, 'admin')
  end

  def destroy?
    super || has_role?(user, 'admin')
  end
end
