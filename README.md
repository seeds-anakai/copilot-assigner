# copilot-assigner

プルリクエストの作成時とドラフト解除時、GitHub Copilotをレビュアーとして追加する。

## 手順

1. プルリクエストの書き込み権限を持つパーソナルアクセストークンを発行する。

2. このリポジトリをコンテナイメージとしてビルドし、ECR に push したうえで、そのイメージを使用する Lambda 関数をデプロイする。

   - このリポジトリを元に Docker イメージを build する。
   - build したイメージを Amazon ECR リポジトリに push する。
   - Lambda 関数のコンテンツとして、上記の ECR イメージを指定する。
   - 環境変数「GH_TOKEN」に上記のトークンを設定する。
   - タイムアウトを「30秒」に設定する。
   - 関数URLを発行する。

3. リポジトリのWebhookに上記の関数URLを設定する。

   - Content-Typeには「application/json」を指定する。
   - 対象のイベントには「Pull requests」を設定する。（※「Pushes」は不要です）
