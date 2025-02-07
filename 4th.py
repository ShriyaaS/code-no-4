def minimizeTicketCost(ticket_price, K):
    stack = []
    
    
    for digit in ticket_price:
        
        
        while K > 0 and stack and stack[-1] > digit:
            stack.pop()
            K -= 1
        
        
        stack.append(digit)
    
   
    while K > 0:
        stack.pop()
        K -= 1
    
    
    result = ''.join(stack).lstrip('0')
    
   
    return result if result else '0'


ticket_price = "203"
K = 2


min_cost = minimizeTicketCost(ticket_price, K)
print(min_cost)  
