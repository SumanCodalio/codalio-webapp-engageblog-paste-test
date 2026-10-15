require_relative 'config/environment'
require 'rhino/commands/install_command'

module Rhino
  module Commands
    class InstallCommand
      def multi_select(prompt)
        if prompt.include?("Which features")
          ["publish", "multi_tenant", "audit_trail"]
        elsif prompt.include?("Install Rhino AI Skill")
          []
        end
      end
      
      def select(prompt)
        "minitest"
      end
      
      def ask(prompt, options = {})
        if prompt.include?("column should be used")
          "slug"
        elsif prompt.include?("roles should your app have")
          "admin, content_team_member"
        end
      end
      
      def yes?(prompt)
        false
      end
    end
  end
end

Rhino::Commands::InstallCommand.new.perform
