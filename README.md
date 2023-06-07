# DevPlatForm
Репозиторий [https://github.com/AveCaesar17/DevPlatForm.git](https://github.com/AveCaesar17/DevPlatForm.git) содержит Ansible-роли, предназначенные для быстрого и удобного разворота платформы безопасной разработки. Чтобы развернуть данную платформу, вам понадобится установленный Ansible на вашей системе.

Для начала развертывания платформы безопасной разработки вам нужно заполнить файл инвентаризации, который содержит адреса серверов и данные для подключения к ним по протоколу SSH. Также вам необходимо заполнить файл с переменными, где указываются настройки, такие как пароли для сервисов, домены и порты.

После заполнения файлов инвентаризации и переменных вы можете выполнить следующую команду в корневой директории репозитория:

```
ansible-playbook ./install_platform.yaml -i /path/to/inventory
```

Замените `/path/to/inventory` на путь к вашему файлу инвентаризации. После выполнения команды Ansible начнет разворачивать платформу безопасной разработки на указанных серверах. Обратите внимание на вывод логов, где будут отображены аутентификационные данные от сервиса DefectDojo.

Пожалуйста, обратите внимание, что при развертывании платформы безопасной разработки из данного репозитория вы должны быть внимательны к безопасности и защите конфиденциальных данных. Убедитесь, что обрабатываете и храните аутентификационные данные согласно соответствующим политикам безопасности вашей организации.