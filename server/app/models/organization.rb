# frozen_string_literal: true

class Organization < Rhino::RhinoModel
  def self.base_owner?
    true
  end

  has_many :user_roles, dependent: :destroy
  has_many :users, through: :user_roles
  has_many :roles, through: :user_roles

  validates :name, presence: true
  validates :slug, presence: true, uniqueness: true

  before_validation :generate_slug, on: :create

  private

  def generate_slug
    self.slug ||= name&.parameterize
  end
end
