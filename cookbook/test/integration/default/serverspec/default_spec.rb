# Encoding: utf-8
require_relative 'spec_helper'

describe 'deploys application' do
  it { expect(page_returns).to match('204') }
end
