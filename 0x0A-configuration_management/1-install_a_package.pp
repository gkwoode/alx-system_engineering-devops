# Install puppet-lint

package { 'pip3':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  unless  => '/usr/bin/pip3 freeze | grep Flask | grep -q 2.1.0',
}

