# This file executes a command with puppet

exec { 'pkill -f killmenow':
  path  => 'usr/bin/:/ur/local/bin/:/bin/',
}
