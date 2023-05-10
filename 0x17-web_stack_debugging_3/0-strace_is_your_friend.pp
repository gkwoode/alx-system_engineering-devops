# Why Apache is returning a 500 error

$file_to_edit = '/var/www/html/wp-settings.php'

# Fixes bad `phpp` extensions to `php`

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin','/usr/bin']
}
