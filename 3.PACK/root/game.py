# add import

import uidungeonreward

# find
	def __init__(self, stream):
		ui.ScriptWindow.__init__(self, "GAME")
		self.SetWindowName("game")
		net.SetPhaseWindow(net.PHASE_WINDOW_GAME, self)
		player.SetGameWindow(self)

# add under


		self.wndDungeonReward = uidungeonreward.ZindanOdulLWT()

# add random or end

	def odulgeldi(self, veri):
		veri = veri.split("|")
		if veri[0] == "guiac":
			self.wndDungeonReward.Show()
		elif veri[0] == "itemgeldi":
			self.wndDungeonReward.SlotuYukle(int(veri[1]),int(veri[2]),int(veri[3]))


# find

		self.serverCommander=stringCommander.Analyzer()

## add over

		serverCommandList["odulgeldi"] = self.odulgeldi

# find

	def OnUpdate(self):	
		app.UpdateGame()

# add under

		if translate.dgacik == 1:
			self.wndDungeonReward.OnUpdate()