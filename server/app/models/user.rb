# frozen_string_literal: true

class User < Rhino::RhinoModel
  include Rhino::HasPermissions
  include Rhino::HasAuditTrail

  has_secure_password
  has_secure_token :api_token

  has_many :user_roles, dependent: :destroy
  has_many :organizations, through: :user_roles
  has_many :roles, through: :user_roles

  validates :name, presence: true
  validates :email, presence: true, uniqueness: true

  rhino_additional_hidden :api_token
  rhino_audit_exclude :api_token, :password_digest
  
  rhino_filters :email, :approved, :profile_completed
  rhino_search :name, :email, :first_name, :last_name
  rhino_sorts :created_at, :name
  rhino_includes :user_roles, 'user_roles.organization', 'user_roles.role'
  rhino_default_sort '-created_at'
end
