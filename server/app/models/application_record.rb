class ApplicationRecord < ActiveRecord::Base
  primary_abstract_class

  def self.resource_owned_by
    :organization
  end

  def self.owner_class
    Organization
  end
end
