# This file fixes the bad "phpp" extensions to "php" in "wp-settings.php" file.

exec{'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
