# DD初期構築手順

# ホスト名設定
net show hostname
net set hostname $HostName
net show hostname
> ホスト名がDWS通りであることを確認する。

# ドメイン名設定
net show domainname
net set domainname $DomainName
net show domainname
> ドメイン名がDWS通りであることを確認する。

# DGW設定
route show gateway
route set gateway $DefaultGateway
route show gateway
> デフォルトゲートウェイがDWS通りであることを確認する。

