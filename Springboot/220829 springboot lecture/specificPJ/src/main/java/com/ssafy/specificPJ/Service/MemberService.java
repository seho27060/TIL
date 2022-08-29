package com.ssafy.specificPJ.Service;

import com.ssafy.specificPJ.Domain.DTO.MRDTO;
import org.springframework.web.bind.annotation.RequestParam;

public interface MemberService {
    public void saveMember(MRDTO member);

    public void updateMember(Long index, MRDTO member);
}
