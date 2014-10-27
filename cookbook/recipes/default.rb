# Encoding: utf-8
#
# Cookbook Name:: binarytree_test
# Recipe:: default
#
# Copyright 2014, Rackspace Hosting
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

site_name = 'example.com'
port = '80'

node.default['pythonstack']['nginx']['sites'][port][site_name]['uwsgi_port'] = 20_001
node.default['pythonstack']['nginx']['sites'][port][site_name]['uwsgi_stats_port'] = '1717'
node.default['pythonstack']['nginx']['sites'][port][site_name]['uwsgi_options'] = {}
node.default['pythonstack']['nginx']['sites'][port][site_name]['uwsgi_template'] = 'nginx/uwsgi.ini.erb'
node.default['pythonstack']['nginx']['sites'][port][site_name]['uwsgi_cookbook'] = 'pythonstack'
node.default['pythonstack']['nginx']['sites'][port][site_name]['template'] = "nginx/sites/#{site_name}-#{port}.erb"
node.default['pythonstack']['nginx']['sites'][port][site_name]['cookbook'] = 'pythonstack'
node.default['pythonstack']['nginx']['sites'][port][site_name]['server_name'] = site_name
node.default['pythonstack']['nginx']['sites'][port][site_name]['server_alias'] = ["test.#{site_name}", "www.#{site_name}"]
node.default['pythonstack']['nginx']['sites'][port][site_name]['docroot'] = "/var/www/#{site_name}/#{port}"
node.default['pythonstack']['nginx']['sites'][port][site_name]['errorlog'] = "#{node['nginx']['log_dir']}/#{site_name}-#{port}-error.log info"
node.default['pythonstack']['nginx']['sites'][port][site_name]['customlog'] = "#{node['nginx']['log_dir']}/#{site_name}-#{port}-access.log combined"
node.default['pythonstack']['nginx']['sites'][port][site_name]['loglevel'] = 'warn'
node.default['pythonstack']['nginx']['sites'][port][site_name]['app'] = 'wsgi:application'
node.default['pythonstack']['nginx']['sites'][port][site_name]['revision'] = 'v1.0.0'
node.default['pythonstack']['nginx']['sites'][port][site_name]['repository'] = 'https://github.com/prometheanfire/binarytree_test'
node.default['pythonstack']['nginx']['sites'][port][site_name]['deploy_key'] = '/root/.ssh/id_rsa'

include_recipe 'pythonstack::application_python'
