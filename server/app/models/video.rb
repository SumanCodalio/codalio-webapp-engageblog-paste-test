# frozen_string_literal: true

class Video < Rhino::RhinoModel
  include Rhino::BelongsToOrganization
  include Discard::Model

  belongs_to :post, class_name: 'Post', optional: true
  belongs_to :user, class_name: 'User'

  rhino_filters :title, :url, :duration, :post_id, :user_id
  rhino_sorts :title, :url, :duration, :post_id, :user_id, :created_at
  rhino_fields :id, :title, :url, :duration, :post_id, :user_id, :created_at
  rhino_includes :post, :user
  validates :title, length: { maximum: 255 }, allow_nil: true
  validates :url, length: { maximum: 255 }, allow_nil: true
  validates :duration, numericality: { only_integer: true }, allow_nil: true
end
