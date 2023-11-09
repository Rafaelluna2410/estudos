#!/bin/bash

echo "Digite o nome da interface, por exemplo, wg0:"
read interface

ip link add dev "$interface" type wireguard

echo "Digite o endereço da interface, por exemplo, x.x.x.x/x:"
read address

ip address add "$address" dev "$interface"

privatekey=$(wg genkey)
publickey=$(echo "$privatekey" | wg pubkey)
echo "$publickey" > "publickey.txt"
echo "$privatekey" > "privatekey.txt"

echo "Digite a rede que será aceita, por exemplo, 10.0.0.0/24:"
read network1

echo "Digite o IP e a porta do endpoint, por exemplo, x.x.x.x:51820:"
read endpoint
echo "Digite a PublicKey do endpoint:"
read pubendpoint
echo "Digite o nome do arquivo de configuração, por exemplo, name.conf:"
read name
echo "
[Interface]
PrivateKey = ${privatekey}
ListenPort = 51820
[Peer]
PublicKey = ${pubendpoint}
AllowedIPs = ${network1}
Endpoint = ${endpoint}" > "${name}"

wg setconf "$interface" "$name"
ip link set up dev  "$interface"
echo "para conectar a uma nova rede, basta adicionar no arquivo de configuração criado e criar uma rota estática" > readme.txt
wg show
echo "foi gerado readem, publickey e privatekey"
