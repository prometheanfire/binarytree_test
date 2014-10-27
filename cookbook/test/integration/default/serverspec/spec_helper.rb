# Encoding: utf-8
require 'serverspec'
require 'net/http'

set :backend, :exec
set :path, '/sbin:/usr/local/sbin:/bin:/usr/bin:$PATH'

def page_returns(url = 'http://localhost/', host = 'example.com')
  uri = URI.parse(url)
  json_body = '{"supertree": {"value": 1,"left": {"value": 5,"right":{"value": 3}},"right":
               {"value": 4,"left": {"value": 2},"right": {"value": 5,"left": {"value": 0},"right":
               {"value": 8}}}},"subtree": {"value": 4,"right": {"value": 5}}}'
  http = Net::HTTP.new(uri.host, uri.port)
  req = Net::HTTP::Post.new(uri.request_uri)
  req.body = json_body
  req.initialize_http_header('Host' => host)
  http.request(req).code
end
