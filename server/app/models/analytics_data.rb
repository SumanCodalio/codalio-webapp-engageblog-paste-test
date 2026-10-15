# frozen_string_literal: true

class AnalyticsData < Rhino::RhinoModel
  include Rhino::BelongsToOrganization
  include Discard::Model

  belongs_to :post, class_name: 'Post'

  rhino_filters :event_type, :recorded_at, :post_id
  rhino_sorts :event_type, :recorded_at, :post_id, :created_at
  rhino_fields :id, :event_type, :event_data, :recorded_at, :post_id, :created_at
  rhino_includes :post
  validates :event_type, length: { maximum: 255 }, allow_nil: true
end
