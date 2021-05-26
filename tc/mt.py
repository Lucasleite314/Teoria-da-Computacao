def delta(mt, estado, simbolo):
    try:
        prox_estado, novo_simbolo, direcao = mt[3][(estado,simbolo)]
        return prox_estado, novo_simbolo, direcao
    except:
        return(None,None,None)


#57 Movimento da MT (Lucas Leite)  #usando funções usadas no desafio Extra MT-1
def do_step(self):
        # Read from tape
        try:
            delta = self.get_cur_delta()
        except KeyError:
            print('Failed at tape state ' + self.print_tape() +
                  ', Automata state ' + str(self.cur_state) +
                  ', tape position ' + str(self.cur_tape_index))
            return False

        # Write to tape
        self.write_char(delta[1])

        # Switch automata state
        self.cur_state = delta[0]

        # Checking if the machine is halted
        if delta[0] in self.tm.Z:
            return False

        # Walk tape
        self.walk_tape(delta[2])

        return True

