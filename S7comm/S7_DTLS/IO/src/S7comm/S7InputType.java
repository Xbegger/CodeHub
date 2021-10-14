package S7comm;

public enum S7InputType {
    JOB, ACK, ACK_DATA, USER_DATA

    public static S7InputType fromProtocolMessageType(ProtocolMessageType type){
        switch(type){
            case JOB:
                return S7InputType.JOB;
            case ACK:
                return S7InputType.ACK;
            case ACK_DATA:
                return S7InputType.ACK_DATA;
            case USER_DATA:
                return S7InputType.USER_DATA;
            default:
                throw new RuntimeException("Type not supported:" + type);
        }
    }


}
