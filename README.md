# ２_PortfolioLambdaについて

## 概要

* API GatewayとLambdaを使った環境構築について、CloudFormationでテンプレート化したものを複数記録。  
&emsp;詳細は以下のとおり、別記。

## CircleCIの利用
&emsp;次のとおり、workflowで環境構築を自動化  
&emsp;workflowの内容
1. リポジトリにコードをpush
2. CircleCIがリポジトリにpushされたことをイベントトリガーとしてworkflowを実行
3. jobとしてCloudFormationを実行

  
## ポートフォリオ番号
1. [**CloudFormaiton1(CURLでDynamoDBのCRUD操作)**](/CloudFormation１.md)
2. [**CloudFormaiton2(ブラウザーからURL入力で、DynamoDBの値を入手)**](/CloudFormation2.md)

