#!/usr/bin/pup
# install puppet-lint using Puppet
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
