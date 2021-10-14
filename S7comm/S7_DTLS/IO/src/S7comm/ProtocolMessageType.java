package S7comm;

import java.util.HashMap;
import java.util.Map;

public enum ProtocolMessageType {
    JOB((byte) 1),
    ACK((byte) 2),
    ACK_DATA((byte) 3),
    USER_DATA((byte) 7);


    private byte value;
    private ProtocolMessageType(byte value){ this.value = value;}

    private static final Map<Byte, ProtocolMessageType> MAP;

    static {
        MAP = new HashMap<>();
        for( ProtocolMessageType cm : ProtocolMessageType.values()){
            MAP.put(cm.value, cm);
        }
    }

    public static ProtocolMessageType getContentType(byte value){ return MAP.get(value); }

    public byte getValue() { return value; }

    public byte[] getArrayValue(){ return new byte[] { value }; }
}
