# robosys2020_kadai2
ロボットシステム学の第2回目の課題です。第10回目に作成したROSのパッケージに一桁の素数(2,3,5,7)の倍数があるのかを表示するプログラムを加えました。
2の倍数だと2,3の倍数だと3,5の倍数だと5,7の倍数だと7と表示します。


パブリッシャ

count.py　https://github.com/kaba92/robosys2020_kadai2/blob/main/scripts/count.py

サブスクライバ

twice.py　https://github.com/kaba92/robosys2020_kadai2/blob/main/scripts/twice.py

使用したミドルウェア

・ROS

使用したOS

・Ubuntu 20.04

使用した言語

・Python3

実行する方法

・端末を3つ用意する。

・一つ目の端末に以下のコマンドを入力する。

 `roscore`

・二つ目の端末に以下のコマンドを順に入力し、count.pyを実行する。

`chmod +x count.py`

`rosrun mypkg count.py`


・三つ目の端末に以下のコマンドを入力し、twice.pyを実行する。

`rosrun mypkg twice.py`

ライセンス　https://github.com/kaba92/robosys2020_kadai2/blob/main/LICENSE


実行したときの動画　https://www.youtube.com/watch?v=swUd-xrw934
