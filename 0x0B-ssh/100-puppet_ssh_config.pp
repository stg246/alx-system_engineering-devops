#!/usr/bin/env bash

# This script install Puppet on the system

package { 'openssh-client':
  ensure => installed,
}


# This script modify the SSH client configuration file

file { '/etc/ssh/ssh_config':
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => template('ssh_config.erb'),
}


# This script create a template file (ssh_config.erb) that contains the configuration options

Host *
  IdentityFile ~/.ssh/school
  PasswordAuthentication no


# This script displays the full Puppet manifest

package { 'openssh-client':
  ensure => installed,
}

file { '/etc/ssh/ssh_config':
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => template('ssh_config.erb'),
}

# Template file
file { '/etc/puppetlabs/code/environments/production/modules/ssh/templates/ssh_config.erb':
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "Host *\n  IdentityFile ~/.ssh/school\n  PasswordAuthentication no\n",
}
