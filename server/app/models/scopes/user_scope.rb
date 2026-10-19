module Scopes
  class UserScope < Rhino::ResourceScope
    def apply(relation)
      if organization
        relation.joins(:user_roles).where(user_roles: { organization_id: organization.id }).distinct
      else
        relation
      end
    end
  end
end
