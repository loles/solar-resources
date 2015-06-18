$ip = hiera('{{ name }}::ip')
$admin_token = hiera('{{ name }}::admin_token')
$db_user = hiera('{{ name }}::db_user')
$db_password = hiera('{{ name }}::db_password')
$db_name = hiera('{{ name }}::db_name')

class {'keystone':
  verbose         => True,
  catalog_type    => 'sql',
  admin_token     => $admin_token,
  sql_connection  => "mysql://$db_user:$db_password@$ip/$db_name",
  public_port     => '{{ port }}'
}