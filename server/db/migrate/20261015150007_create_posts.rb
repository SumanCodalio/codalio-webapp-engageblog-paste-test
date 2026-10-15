# frozen_string_literal: true

class CreatePosts < ActiveRecord::Migration[8.0]
  def change
    create_table :posts do |t|
      t.references :organization, null: false, foreign_key: true
      t.string :title
      t.text :content, null: true
      t.string :status, null: true, default: "draft"
      t.datetime :published_at, null: true
      t.references :user, foreign_key: true
      t.datetime :discarded_at
      t.index :discarded_at
      t.timestamps
    end
  end
end
