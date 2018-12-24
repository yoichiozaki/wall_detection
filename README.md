# wall_detection

- 壁検知用のノード
- `sweep_ros`がパブリッシュしている`/pc2`トピックをサブスクライブして、壁が近くにあるときには`/wall_is_near`トピックに`true`をパブリッシュする
- 「壁が近くにある」の定義は次の通り。
    - ![](https://i.imgur.com/wUxSi68.jpg)

