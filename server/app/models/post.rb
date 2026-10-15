# frozen_string_literal: true

class Post < Rhino::RhinoModel
  include Rhino::BelongsToOrganization

  belongs_to :user, class_name: 'User'
  has_many :videos
  has_many :analytics_data, class_name: 'AnalyticsData'

  rhino_filters :title, :status, :published_at, :user_id
  rhino_sorts :title, :status, :published_at, :user_id, :created_at
  rhino_fields :id, :title, :content, :status, :published_at, :user_id, :created_at
  rhino_includes :user, :videos, :analytics_data
  validates :title, length: { maximum: 255 }, allow_nil: true
  validates :status, length: { maximum: 255 }, allow_nil: true
end
