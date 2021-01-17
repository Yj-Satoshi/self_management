# 目標管理アプリ
## アプリケーション概要	
月単位の自分の目標と、その目標を実現するためのアクションを記入し目標達成を支援します。また目標及びアクションを設定するにあたりなぜその設定を立てたのかの背景記録、またその設定は適切なものか評価し振り返り反省することで、PDCAサイクルの"P", "C", "A"にあたる過程の質向上にも繋げます。

## URL	
<https://www.yj-selfmanagement-app.tk/>

## テスト用アカウント	
ユーザー名 test1
パスワード 1234test

## 利用方法
1. アカウントを登録します
2. 月単位で達成した目標を設定します(対象の年・月、目標は入力必須)
3. 設定した目標に対して週単位で実施するアクションを設定します(何周目、目標達成のアクションの名称は入力必須)
4. 実際に立てたアクションを実行します
5. アクション並びに目標を評価し、反省点などあれば次の目標・アクションに生かしましょう。

## 目指した課題解決	
大なり小なり誰しも目標や理想を持つことはあると思います。
しかしながら、実際にその目標に対し、最後までやり切って達成できず、挫折してしまったり、目標を達成しても、振り返ればもっと上手くやれたと思うことが多いと思います。

上記の問題は目標に対する
* どのタイミングで何をするのか、どんなアクションが必要なのか(具体的アクションプランの選定)
* なぜそのアクションをする必要があるのか(アクションプランの妥当性の考慮)
* また実際に行動してどうだったか (今までの過程の評価・反省)
を考える過程を飛ばして、闇雲に行動したこのによる結果と考えます。

このアプリケーションでは上記の３点の過程を踏まえた目標管理を行うことで、
目標達成率の向上や目標達成の為のPDCAサイクル質の向上を目的としています。

## 洗い出した要件	
* アカウント登録
* 目標投稿機能
* アクション投稿機能
* 目標投稿編集・削除機能
* アクション投稿編集・削除機能
* 今月のカレンダー表示機能
* 今週のカレンダー表示機能
* 今週のアクションの一覧表示
* ページネーション機能
* メッセージフレームワーク機能
* 評価の成績表示 
* 天気予報表示機能
* 自分の目標関連する他のユーザの目標・アクションの共有化


## 実装した機能について
* 月単位の目標の設定と評価(投稿・編集・削除)
* 週単位の目標達成のアクションの設定と評価(投稿・編集・削除)及び対象の目標内での表示
* 今月のカレンダー表示
* 今週のカレンダー表示
* 今週取り組むべきアクション一覧表示
* 評価済み目標と未評価目標のページ分離
* アカウント登録とログイン機能実装
* ページネーション機能実装
* メッセージフレームワーク機能
   - 投稿・評価後にメッセージ表示
   - 目標設定後はアクション設定を促す。（"目標作成しました。次はアクションを作成下さい"）
   - アクション設定後は行動を促す。（'アクション作成しました。作成したアクションを実施下さい（P "D" CA）'）
   - 評価後は評価によってメッセージを表示する。(以下、一部例)   
     - 通常評価→今後も頑張りましょう("目標を評価しました。次の目標も頑張りましょう")
     - 低評価→反省点を今後に活かしましょう（"目標を評価しました。反省点を無駄にせず、次の目標に切替えましょう"）

## 実装予定の機能	
* matplotlibによる評価点の推移グラフ実装
* BeautifulSoupによる天気予報のWEBスクレイピングのDBもしくはCSVファイル保存と週間カレンダーへの連携表示
* 自分の目標関連する他のユーザの目標とアクションのランダム抽出表示(他者の参考)

## データベース設計

### custom_user テーブル
| Column     | Type    | Options     |
| ---------- | ------- | ------------|
| username   | string  | null: false |
| password   | string  | null: false |
| e-mail     | string  | null: false |
| birth_year | integer | null: false |
| address    | string  |             |
| gender     | string  |             |
| profession | string  |             |

### Association

- has_many :montyly_goal
- has_many :weekly_action


### monthly_goal テーブル
| Column         | Type       | Options                        |
| -------------- | ---------- | -------------------------------|
| year           | integer    | null: false                    |
| month          | integer    | null: false                    |
| category       | string     | null: false                    |
| goal           | string     | null: false                    |
| revised_goal   | string     |                                |
| score          | integer    |                                |
| why_need_goal  | text       |                                |
| why_revise     | text       |                                |
| after_memo     | text       |                                |
| custom_user_id | references | null: false, foreign_key: true |

### Association

- belongs_to :custom_user
- has_many   :weekly_action


### monthly_goal テーブル
| Column            | Type       | Options                        |
| ----------------- | ---------- | -------------------------------|
| week_no           | integer    | null: false                    |
| goal_action       | string     | null: false                    |
| score             | integer    |                                |
| why_select_action | text       |                                |
| after_memo        | text       |                                |
| custom_user_id    | references | null: false, foreign_key: true |
| monthly_goal_id   | references | null: false, foreign_key: true |

### Association

- belongs_to :custom_user
- belongs_to :monthly_goal

## ローカルでの動作方法	
動作必要環境 
* docker(version 20.10.2 動作確認済み)
* docker-compose(version 1.27.4 動作確認済み) 

コマンド (docker-compose.ymlのあるディレクトリにて)
docker-compose up