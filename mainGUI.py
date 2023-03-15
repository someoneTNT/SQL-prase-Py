# author: dzj
# date: 2023-03-08
# desc: 输入框设计

import wx
import recognitionInput as rip
import transform as tfm

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(850, 750))
        
        # 创建一个垂直布局
        vbox = wx.BoxSizer(wx.HORIZONTAL)
        
        # 创建一个大的输入框
        self.input_text = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(350, 700))
        vbox.Add(self.input_text, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)        
        
        # 创建一个转换按钮
        self.convert_button = wx.Button(self, label='转换', size=(50, 30))
        self.convert_button.Bind(wx.EVT_BUTTON, self.on_convert)
        vbox.Add(self.convert_button, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)

        # 创建一个同等大小的输出框
        self.output_text = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(350, 700))
        vbox.Add(self.output_text, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        
        
        # 将布局应用到窗口中
        self.SetSizer(vbox)
        
        # 显示窗口
        self.Show(True)
        
    def on_convert(self, event):
        # 在这里实现转换逻辑
        input_text = self.input_text.GetValue()
        sql_list=rip.recSQL(input_text)
        output_text = tfm.transContent(sql_list)
        self.output_text.SetValue(output_text)


if __name__ == "__main__":
    sql='''       
        insert into tabB 
        select * from tabA;
        -- 测试demo
        select * from tabB
    '''
    # sql_list=rip.recSQL(sql)
    # print(transContent(sql_list)) 
    app = wx.App(False)
    frame = MyFrame(None, "转换程序")
    app.MainLoop() # type: ignore
