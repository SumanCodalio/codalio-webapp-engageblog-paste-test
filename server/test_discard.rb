require_relative 'config/environment'
class Post
  default_scope -> { kept }
end
puts "Discarded count: #{Post.unscoped.discarded.count}"
puts "Trashed endpoint uses model_class.discarded: #{Post.discarded.count}"
