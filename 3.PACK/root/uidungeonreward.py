## @LWT ##

import ui, uiToolTip, net, app, translate

KART_ADET = 4

class ZindanOdulLWT(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.zaman = 0
		self.gosterzaman = 3
		self.LoadWindow()

	def __del__(self):
		ui.Window.__del__(self)

	def Close(self):
		if self.cardboss.IsShow():
			self.Show()

	def Show(self):
		if self.cardboss.IsShow():
			self.cardboss.Hide()
		else:
			self.cardboss.Show()

	def LoadWindow(self):

		self.cardboss = ui.ImageBox()
		self.cardboss.SetCenterPosition(-250, -200)
		self.cardboss.AddFlag("movable")
		self.cardboss.AddFlag("float")
		self.cardboss.LoadImage("lwt/kartlar/kart_odul.png")
		self.cardboss.Hide()

		self.tooltipItem = uiToolTip.ItemToolTip()
		self.tooltipItem.Hide()
		
		self.bg = {}
		for i in xrange(KART_ADET):
			self.bg[i] = {}
			self.bg[i]["image"] = ui.ImageBox()
			self.bg[i]["image"].SetParent(self.cardboss)
			self.bg[i]["image"].SetPosition(110*i, 160)
			self.bg[i]["image"].LoadImage("lwt/kartlar/normal_kart.png")
			self.bg[i]["image"].SAFE_SetMouseClickEvent(self.GetReward,i)
			self.bg[i]["image"].Show()

			self.bg[i]["grid"] = ui.GridSlotWindow()
			self.bg[i]["grid"].SetParent(self.cardboss)
			if i == 0:
				self.bg[i]["grid"].SetPosition(35, 180)
			else:
				self.bg[i]["grid"].SetPosition(55*(i+i)+35, 180)
			self.bg[i]["grid"].ArrangeSlot(0,1,1,96,32,10,0)
			self.bg[i]["grid"].RefreshSlot()
			self.bg[i]["grid"].Hide()

	def GetReward(self,x):
		if translate.dgacik == 1:
			import chat
			chat.AppendChat(1, "Zaten odul almissin.")
		else:
			self.bg[x]["image"].Hide()
			self.bg[x]["image"].LoadImage("lwt/kartlar/item_karti.png")
			self.bg[x]["image"].Show()

			net.SendChatPacket("/odulsectim %d" % (x))
			self.bg[x]["grid"].Show()
			translate.dgacik = 1
			self.zaman = app.GetTime() + 5

			for j in xrange(KART_ADET):
				if j == x:
					continue
				self.bg[j]["image"].Hide()
				self.bg[j]["image"].LoadImage("lwt/kartlar/item_karti_cikmayan.png")
				self.bg[j]["image"].Show()
				self.bg[j]["grid"].Show()

	def SlotuYukle(self, slot, vnum, miktar):
		self.bg[slot]["grid"].SetItemSlot(0,vnum,miktar)

	def OnUpdate(self):
		if app.GetTime() > self.zaman:
			self.cardboss.Hide()
			translate.dgacik = 0