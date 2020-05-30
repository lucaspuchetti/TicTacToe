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
    public String getName() {
        return name;
    }

    public Character getSymbol() {
        return symbol;
    }

    public void setSymbol(Character symbol) {
        this.symbol = symbol;
    }

    public Set<Byte> getSlots() {
        return slots;
    }

    public void addSlot(byte slot) {
        this.slots.add(slot);
    }

    public void resetSlots(){
        this.slots = new HashSet<Byte>();
    }
}
