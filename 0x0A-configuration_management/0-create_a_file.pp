# This Puppet manifest ensures the creation of a file with specific attributes.
file { '/tmp/school':
    ensures => 'file',
    content => 'I love Puppet'
    mode    => '0744'
    owner   => 'www-data'
    group   => 'www-data'
}
