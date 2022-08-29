package com.practice.prac1.Service;

import com.practice.prac1.Domain.DTO.MemberReqDTO;
import com.practice.prac1.Domain.DTO.MemberResDTO;

public interface MemberService {
    void saveMember(MemberReqDTO member);

    void updateMember(Long index, MemberReqDTO memberReqDTO);

    Long deleteMember(Long index);

    MemberResDTO readMember(Long index);
}
