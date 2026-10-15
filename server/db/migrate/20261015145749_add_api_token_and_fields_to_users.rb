class AddApiTokenAndFieldsToUsers < ActiveRecord::Migration[8.1]
  def change
    add_column :users, :api_token, :string
    add_index :users, :api_token, unique: true
    add_column :users, :approved, :boolean
    add_column :users, :profile_completed, :boolean
    add_column :users, :first_name, :string
    add_column :users, :last_name, :string
  end
end
