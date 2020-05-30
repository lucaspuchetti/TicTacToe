package TicTacToe;

import java.util.HashSet;
import java.util.Set;

class Player {
    // Properties
    private String name;
    private Character symbol;
    private Set<Byte> slots = new HashSet<Byte>();

    // Constructor
    public Player(String name , Character symbol){
        this.name = name;
        this.symbol = symbol;
    }

    // Methods
    protected String getName() {
        return name;
    }

    protected Character getSymbol() {
        return symbol;
    }

    protected void setSymbol(Character symbol) {
        this.symbol = symbol;
    }

    protected Set<Byte> getSlots() {
        return slots;
    }

    protected void addSlot(byte slot) {
        this.slots.add(slot);
    }

    protected void resetSlots(){
        this.slots = new HashSet<Byte>();
    }
}
