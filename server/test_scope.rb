require_relative 'config/environment'
module Scopes
  class PostScope < Rhino::ResourceScope
    def apply(relation)
      relation.kept
    end
  end
end
puts "Trashed count: #{Post.discarded.count}"
