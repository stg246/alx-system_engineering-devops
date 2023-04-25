file { '/root/.ssh/config':
  content => "Host example.com\n\
              IdentityFile ~/.ssh/school\n\
              PasswordAuthentication no\n",
}

