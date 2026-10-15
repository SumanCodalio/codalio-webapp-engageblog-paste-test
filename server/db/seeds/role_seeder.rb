# frozen_string_literal: true


Role.find_or_create_by!(slug: 'admin') do |r|
  r.name = 'Admin'
  r.description = 'Full access to manage the application, settings, integrations, and users.'
end

Role.find_or_create_by!(slug: 'content_team_member') do |r|
  r.name = 'Content Team Member'
  r.description = 'Access to create, edit, and publish blog posts, upload videos, and view analytics.'
end
