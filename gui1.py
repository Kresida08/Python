import tkinter as tr
from tkinter import messagebox

class account:
    def __init__ (self,username,acct,Amt):
        self.username= username
        self.acct=acct
        self.balance=Amt

    def display(self):
        print(f"Hello {self.username} your account number {self.acct} has balance {self.balance}. Thank You")
    
    def debit(self, db):
     if db > self.balance:
        return "Not Sufficient Balance"
     self.balance=self.balance-db
     return f"₹{db:.2f} withdrawn. Current balance: ₹{self.balance:.2f}"


    def credit(self, cr):
     self.balance=self.balance+cr
     return f"₹{cr:.2f} deposited. Current balance: ₹{self.balance:.2f}"


class BankingApp:
        def __init__ (self,root,acct):
          self.root=root
          self.acct=acct
          self.root.title("Banking System")
          self.root.geometry("400x650")
          self.root.resizable(False,False)

# Create Header

          head_frame=tr.Frame(root, bg="#2c3e50", height=75)
          head_frame.pack(fill=tr.X)

          head=tr.Label(head_frame,
                      text="Banking System",
                      font=("Elephant",20,"bold"),
                      bg="#2c3e50",
                      fg="White")
          head.pack(pady=30)
 
# # Account Info

          info_frame=tr.Frame(root, bg="#f0f0f0", height=25)
          info_frame.pack(fill=tr.X)

          info_frame=tr.Label(info_frame,
                      text=f"Welcome,{acct.username}",
                      font=("Elephant",20),
                      bg="#f0f0f0"
                      ).pack(fill=tr.X)
        
          info_frame=tr.Label(info_frame,
                      text=f"Account: {acct.acct}",
                      font=("Arial",18),
                      bg="#f0f0f0"
                      ).pack()
        
# Balance Display

          self.balance_var=tr.StringVar()
          self.update_balance_display()
          
          balance_frame=tr.Frame(root, bg="#ecf0f1", pady=15)
          balance_frame.pack(fill=tr.X)

          tr.Label(balance_frame, 
                      textvariable=self.balance_var,
                      font=("Arial",18,"bold"),
                      bg="#ecf0f1"
                      ).pack()
        
# # Operation Frame

          opr_frame=tr.Frame(root,bg="#f0f0f0", pady=20)
          opr_frame.pack(fill=tr.Y,padx=30)

# # Amount Entry

          amt_frame=tr.Frame(opr_frame, bg="#f0f0f0")
          amt_frame.pack(fill=tr.X, pady=10)
    
          tr.Label(amt_frame,
             text="Amount (\u20B9):",
             font=("Arial",15,"bold"),
             bg="#f0f0f0"
             ).pack(side=tr.LEFT,padx=10)
    
          self.amt=tr.Entry(amt_frame,font=("Arial",12),width=20)
          self.amt.pack(side=tr.LEFT, padx=5)
        
# Buttons

          button_frame=tr.Frame(opr_frame, bg="#f0f0f0")
          button_frame.pack(fill=tr.X, pady=10)

          tr.Button(button_frame,
                  text="Deposit",
                  font=("Arial",15),
                  bg="#f00e0e",
                  fg="white",
                  padx=25,
                  pady=15,
                  command=self.deposit
                  ).pack(side=tr.LEFT, padx=15)
        
          tr.Button(button_frame,
                  text="Withdraw",
                  font=("Arial",15),
                  bg="#09ed33",
                  fg="white",
                  padx=25,
                  pady=15,
                  command=self.withdraw
                  ).pack(side=tr.LEFT, padx=15)
        
# # Transaction Hist

          hist_frame=tr.Frame(root, bg="#f0f0f0",pady=10)
          hist_frame.pack(fill=tr.BOTH, expand=True, padx=30)

          tr.Label(hist_frame,
                            text="Transaction History",
                            font=("Arial",15),
                            bg="#f0f0f0",
                            ).pack()
        
# Create a frame with a transaction hist with scroll bar

          self.hist_list_frame=tr.Frame(hist_frame, bg="white", bd=1, relief=tr.SUNKEN)

          self.hist_list_frame.pack(fill=tr.BOTH, expand=True, pady=10)

          self.transaction_hist=tr.Text(self.hist_list_frame, height=7, font=("Arial",10))

          self.transaction_hist.pack(side=tr.LEFT, fill=tr.BOTH, expand=True)

          Scrollbar=tr.Scrollbar(self.hist_list_frame,command=self.transaction_hist.yview)
          Scrollbar.pack(side=tr.RIGHT, fill=tr.Y)

          self.transaction_hist.config(yscrollcommand=Scrollbar.set)

# # # Footer

          foot=tr.Frame(root,bg="#2c3e50", height=40)
          foot.pack(fill=tr.X, side=tr.BOTTOM)

          foot=tr.Label(foot,
                      text="© 2025 Banking System",
                      font=("Arial",10),
                      bg="#2c3e50",
                      fg="White").pack()
        
# Initialize transaction history

          self.add_transaction("account opened")

        def update_balance_display(self):
         self.balance_var.set(f"Balance:\u20B9{self.acct.balance:}")

        def get_amt(self):
           try:
              amount=float(self.amt.get())
              if amount<=0:
                 
                messagebox.showerror("Error","Please enter a positive amount")
                return None
              return amount
           except ValueError:
              
              messagebox.showerror("Error","Please enter a valid amount")
              return None
           
        def withdraw (self):
         amt= self.get_amt()
         if amt:
              result=self.acct.debit(amt)
              if "Not Sufficient" not in result:
                 self.update_balance_display()
                 self.add_transaction(f"Withdrew:{amt:.2f}")
                 messagebox.showinfo("Sucess",result)
                 self.amt.delete(0,tr.END)

        def deposit (self):
         amt= self.get_amt()
         if amt:
          result=self.acct.credit(amt)
          self.update_balance_display()
         self.add_transaction(f"Deposited:{amt:.2f}")
         messagebox.showinfo("Sucess", result)
         self.amt.delete(0,tr.END)

        def add_transaction(self, transaction_text):
           timestamp=tr.StringVar()
           from datetime import datetime
           now=datetime.now()
           timestamp=now.strftime("%H:%M:%S")

           self.transaction_hist.insert("1.0",f"[{timestamp}] {transaction_text}")
           self.transaction_hist.see(tr.END)

# Run the application
if __name__ == "__main__":
               root=tr.Tk()
               user=account("Cecil", 9876543210 , 35000)
               app =BankingApp(root,user)
               root.mainloop()















