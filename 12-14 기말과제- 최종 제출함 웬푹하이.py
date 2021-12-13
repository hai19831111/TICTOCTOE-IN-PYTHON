import random
 
def drawBoard(board):
    #체스판에 인쇄(Thực hiện in ra bàn cờ)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])
 
def inputPlayerLetter():
    #플레이어가 사용하려는 캐릭터를 입력할 수 있도록 허용(Cho phép người chơi nhập ký tự mà họ muốn sử dụng)
    #플레이어가 첫 번째 요소로 선택한 캐릭터와 함께 List 유형의 컬렉션을 반환합니다(Trả về tập hợp kiểu List với ký tự mà người chơi chọn làm phần tử đầu tiên)
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('당신은 X 또는 O가되고 싶습니까?')
        letter = input().upper()
 
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
 
def whoGoesFirst():
    #플레이어가 먼저 갈 수 있도록 무작위로 선택(Chọn ngẫu nhiên bất kỳ cho phép người chơi đi trước hay không)
    if random.randint(0, 1) == 0:
        return '컴퓨터'
    else:
        return '플레이어'
 
def makeMove(board, letter, move):
    board[move] = letter
 
def isWinner(bo, le):
    #플레이어가 이기면 True 반환(Trả về True nếu người chơi thắng)
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or #윗줄 1개
    (bo[4] == le and bo[5] == le and bo[6] == le) or         # 가운데 행
    (bo[1] == le and bo[2] == le and bo[3] == le) or         #마지막줄
    (bo[7] == le and bo[4] == le and bo[1] == le) or         #왼쪽열
    (bo[8] == le and bo[5] == le and bo[2] == le) or         #가운데 기둥
    (bo[9] == le and bo[6] == le and bo[3] == le) or         #오른쪽열
    (bo[7] == le and bo[5] == le and bo[3] == le) or         #대각선
    (bo[9] == le and bo[5] == le and bo[1] == le))
 
def getBoardCopy(board):
    #체스판 복사(Sao chép bàn cờ)
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy
 
def isSpaceFree(board, move):
    #이동이 비어 있으면 True를 반환합니다(Trả về True nếu nước đi còn chỗ trống)
    return board[move] == ' '
 
def getPlayerMove(board):
    #플레이어의 움직임을 잡아라(Lấy nước đi của người chơi)
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('다음 행보는 무엇입니까? (1-9)')
        move = input()
    return int(move)
 
def chooseRandomMoveFromList(board, movesList):
    #유효한 이동을 반환합니다(Trả về một nước đi hợp lệ)
    #유효한 이동이 없으면 None을 반환합니다(Trả về None nếu không còn nước đi hợp lệ)
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
 
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
 
def getComputerMove(board, computerLetter):
    #기계의 물을 결정하십시오(Xác định nước đi cho máy)
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
 
    #게임기용 알고리즘(Giải thuật cho máy chơi)
    #다음 움직임의 승패를 확인(Kiểm tra xem nước đi tiếp theo có thắng được hay không)
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i
 
    #플레이어가 다음 이동에서 이길 수 있는지 확인 (Kiểm tra xem người chơi có thể thắng trong nước đi tiếp theo hay không)
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i
 
    #비어 있는 경우 보드 모서리에서 이동을 선택합니다.(Chọn một nước đi ở các góc bàn cờ nếu trống)
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
 
    #중간에 이동을 선택(Chọn nước đi ở giữa)
    if isSpaceFree(board, 5):
        return 5
 
    #체스 판의 측면에서 움직임 중 하나를 선택하십시오 (Chọn một trong các nước đi ở các cạnh bên của bàn cờ)
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])
 
def isBoardFull(board):
    #움직임이 없으면 True, 그렇지 않으면 False를 반환합니다.(Trả về True nếu các nước đi không còn, ngược lại trả về False)
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True
 
 
print('Welcome to Tic Tac Toe!')
 
while True:
    #체스판 재설정 (Thiết lập lại bàn cờ)
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True
 
    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
 
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('만세! 게임에서 이겼습니다!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('게임은 동점입니다!')
                    break
                else:
                    turn = '컴퓨터'
 
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
 
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('컴퓨터가 당신을 이겼습니다! 당신은 잃는다.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('게임은 동점입니다!')
                    break
                else:
                    turn = '플레이어'
 
    print('다시 플레이하시겠습니까?(yes or no)')
    if not input().lower().startswith('y'):
        break
