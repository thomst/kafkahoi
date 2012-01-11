Um kafkahoi zu spielen muss Python 2.6.4 und Pygame installiert sein.
Python-download: http://www.python.org/ftp/python/2.6.4/python-2.6.4.msi
Pygame-download: http://pygame.org/ftp/pygame-1.9.1.win32-py2.6.msi
(für Windows)

Anleitung für kafkahoi:
	immer:
		's' = Sound ein/aus (wobei der Sound noch ziemlich miserabel ist)
		'esc' = exit

	Menü:
		'p' = Gedichte wählen
		'd' = Schwierigkeit wählen
		'e' = Editor starten

	während des Spielens
		'p' = Pause	

		linke Maustaste = weißer Stern schießt
		rechte Maustaste = fliederfarbene Stern sammelt

		'y'/'c' oder ←/→ = weißer Stern zielt

		SPACE oder ↓ = 	gesammelte Buchstaben werden abgeschleudert:
							wenn die Buchstaben ein Wort des "gesuchten Gedichtes" bilden
							oder schon vorhandene Buchstaben zu einem ganzen Wort
 							ergänzen, dann fallen sie in ihre "Gedicht-Position".
							Sonst landen sie irgendwo und müssen neu gesammelt werden.

		Scrollrad = 	-korrigiert die Richtung des weißen Sterns
						-bei gedrückter recher Maustaste die des fliederfarbenen Sterns


	Ablauf:
		Ziel des Spiels ist es, dass Gedicht zu vervollständigen. Dazu werden die
		Buchstaben gesammelt.
		Die Sterne reagieren auf unterschiedliche und wechselnde Weise auf 
		die Position der Maus.
		Käfer und Fliegen dürfen nicht berührt werden (man verliert ein Leben).
		Der Käfer kann für einige Sekunden durch einen Treffer lahm gelegt werden.
		Die Fliegen werden abgeschossen. Sie bringen weitere Buchstaben. Manchmal auch
		ein Leben, das eingesammelt werden kann oder gar nichts.
