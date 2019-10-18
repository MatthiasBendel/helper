#!/bin/bash
# version 0.9

echo Wählen Sie eine der folgenden Zahlen um einen Befehl auszuführen:
echo
echo "1	:	Audio-Bypass"
echo "2	:	Backup ... @D"
echo "3	:	ssh raspi @D"
echo "4	:	alte Kernel entfernen (Achtung: keine erneute Nachfrage!) @D"
echo "5	:	Häufig genutzte Programme installieren."
echo "6	:	ssh rbg.tu-darmstadt.de ..."
echo "7	:	apt: full-upgrade, autoremove & autoclean @D"
echo "8	:	XAMPP @D"
#echo "9	:	dieses HelperScript aktualisieren"
echo
read r
echo
case "$r" in
	1) echo "parec --latency-msec=1 | pacat --latency-msec=1"
				parec --latency-msec=1 | pacat --latency-msec=1
		;;
		
	2) echo "Welches Backup soll durchgeführt werden?"
		echo "1:	Backup von matze@raspi nach ~/Archiv/Backup/ (exclude ~/Backup)"
		echo "2:	Backup von matze@L540  nach matze@raspi:~/Backup"
		echo "3:	beide vorherige"
		echo "4:	vorhandene Backups anzeigen (@raspi)"
		echo "5:	Log-File anzeigen"
		read r2
		case "$r2" in
			1) rsync --delete --numeric-ids --relative --delete-excluded --exclude=/home/matze/.local/share/Trash/ --exclude=/home/matze/Backup/ --exclude=/home/matze/.cache/ -avze ssh matze@192.168.0.100:/home/matze /home/matze/Archiv/Backup/matze@raspi
				;;
			2) ssh -t raspi sudo ./my_rsnapshot.sh hourly
				;;
			3) rsync --delete --numeric-ids --relative --delete-excluded --exclude=/home/matze/.local/share/Trash/ --exclude=/home/matze/Backup/ --exclude=/home/matze/.cache/ -avze ssh matze@192.168.0.100:/home/matze /home/matze/Archiv/Backup/matze@raspi
				ssh -t raspi sudo ./my_rsnapshot.sh hourly
				;;
			4) ssh raspi ls -lAt Backup/
				;;
			5) ssh raspi tail -23 Backup/rsnapshot.log | less -S
				;;
			*) echo "Eingabe wurde nicht erkannt, bitte versuchen Sie es erneut."
				;;
		esac
		;;
		
	3) ssh raspi
		;;
	4) dpkg -l 'linux-*' | sed '/^ii/!d;/'"$(uname -r | sed "s/\(.*\)-\([^0-9]\+\)/\1/")"'/d;s/^[^ ]* [^ ]* \([^ ]*\).*/\1/;/[0-9]/!d' | xargs sudo apt-get purge -y #"
		;;
	5) cd ~/Dokumente/Installation/; ./Programme_installieren_1.3.sh
		;;
		
	6) echo "Welcher Client soll angesprochen werden?"
		echo "1	:	ssh vp94hyso@clientssh1.rbg.informatik.tu-darmstadt.de -X"
		echo "2	:	ssh vp94hyso@clientssh2.rbg.informatik.tu-darmstadt.de -X"
		echo "3	:	ssh vp94hyso@clientssh3.rbg.informatik.tu-darmstadt.de -X"
		read r2
		case "$r2" in
			1) ssh vp94hyso@clientssh1.rbg.informatik.tu-darmstadt.de -X
				;;
			2) ssh vp94hyso@clientssh2.rbg.informatik.tu-darmstadt.de -X
				;;
			3) ssh vp94hyso@clientssh3.rbg.informatik.tu-darmstadt.de -X
				;;
			*) echo "Eingabe wurde nicht erkannt, bitte versuchen Sie es erneut."
				;;
		esac
		;;
		
	7) sudo apt full-upgrade
		sudo apt autoremove
		sudo apt autoclean
		;;
	8) gksudo /opt/lampp/manager-linux-x64.run
		;;
#	9)	cd ~/bin/
#			mv h h_backup
#			wget https://www.dropbox.com/s/052fdg0dbjegbob/h?dl=1
#			mv h?dl=1 h
#			chmod +x h
#		;;
	*) echo "Eingabe wurde nicht erkannt, bitte versuchen Sie es erneut."
	;;
esac


# alte Befehle:
# Bachelorpraktikumsserver
# ssh matthias@vm6.rbg.informatik.tu-darmstadt.de
# Push and Commit Thesis
#cd ~/workspace/ErrDapt/thesis
#		./pushAndCommit.sh
